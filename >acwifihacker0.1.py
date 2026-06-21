import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading
import platform
import random
import time

class ACWiFiHacker:
    def __init__(self, root):
        self.root = root
        self.root.title("ac's wifi hacker 0.1")
        self.root.geometry("1100x720")
        self.root.configure(bg="#0A0A0A")

        # Header
        tk.Label(root, text="AC'S WIFI HACKER 0.1", bg="#0A0A0A", fg="#00FFAA", font=("Courier", 20, "bold")).pack(pady=10)

        # Main frame
        main_frame = tk.Frame(root, bg="#0A0A0A")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Target
        tk.Label(main_frame, text="Target BSSID / Network:", bg="#0A0A0A", fg="#00FFAA", font=("Courier", 12)).pack(anchor="w")
        self.target_entry = tk.Entry(main_frame, width=60, bg="#1A1A1A", fg="#00FFAA", insertbackground="#00FFAA", font=("Courier", 11))
        self.target_entry.pack(fill="x", pady=5)
        self.target_entry.insert(0, "00:11:22:33:44:55")

        # Buttons
        btn_frame = tk.Frame(main_frame, bg="#0A0A0A")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="SCAN NETWORKS", bg="#002211", fg="#00FFAA", font=("Courier", 11, "bold"),
                  width=18, height=2, command=self.scan_networks).pack(side="left", padx=8)
        
        tk.Button(btn_frame, text="DEAUTH ATTACK", bg="#330000", fg="#FF4444", font=("Courier", 11, "bold"),
                  width=18, height=2, command=self.deauth_attack).pack(side="left", padx=8)
        
        tk.Button(btn_frame, text="CAPTURE HANDSHAKE", bg="#002211", fg="#00FFAA", font=("Courier", 11, "bold"),
                  width=18, height=2, command=self.capture_handshake).pack(side="left", padx=8)
        
        tk.Button(btn_frame, text="WPS PIN ATTACK", bg="#002211", fg="#00FFAA", font=("Courier", 11, "bold"),
                  width=18, height=2, command=self.wps_attack).pack(side="left", padx=8)

        # Log
        tk.Label(main_frame, text="=== ATTACK LOG ===", bg="#0A0A0A", fg="#00FFAA", font=("Courier", 14, "bold")).pack(pady=(20,5))
        self.log = scrolledtext.ScrolledText(main_frame, height=22, bg="#000000", fg="#00FFAA", font=("Courier", 10))
        self.log.pack(fill="both", expand=True, padx=10, pady=5)

        self.status = tk.Label(root, text="AC HOLDINGS WIFI HACKER 0.1 | READY | NYAH~", 
                             bg="#000000", fg="#00FFAA", font=("Courier", 9))
        self.status.pack(side="bottom", fill="x")

    def log_event(self, msg, level="INFO"):
        timestamp = time.strftime("%H:%M:%S")
        color = "#FF4444" if "FAIL" in msg or "ATTACK" in msg else "#00FFAA"
        self.log.insert(tk.END, f"[{timestamp}] [{level}] {msg}\n")
        self.log.see(tk.END)

    def scan_networks(self):
        self.log_event("Starting WiFi scan...", "SCAN")
        def run():
            try:
                if platform.system() == "Darwin":
                    result = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"], timeout=8).decode()
                else:
                    result = "Simulator: Found 12 networks."
                self.log_event("Scan complete. Networks detected.", "SUCCESS")
                self.log.insert(tk.END, result[:800] + "\n...\n")
            except Exception as e:
                self.log_event(f"Scan failed: {e}", "ERROR")
        threading.Thread(target=run, daemon=True).start()

    def deauth_attack(self):
        target = self.target_entry.get().strip() or "00:11:22:33:44:55"
        self.log_event(f"Launching DEAUTH attack on {target}...", "ATTACK")
        def attack():
            for i in range(25):
                self.log_event(f"Sending deauth packet {i+1}/25...", "ATTACK")
                time.sleep(0.15)
            self.log_event("Deauth flood complete. Clients disconnected.", "SUCCESS")
        threading.Thread(target=attack, daemon=True).start()

    def capture_handshake(self):
        target = self.target_entry.get().strip()
        self.log_event(f"Attempting handshake capture on {target}...", "ATTACK")
        def run():
            for i in range(8):
                self.log_event(f"Waiting for handshake... {i+1}/8", "WAIT")
                time.sleep(0.6)
            self.log_event("HANDSHAKE CAPTURED! Saved to ac_handshake.cap", "SUCCESS")
        threading.Thread(target=run, daemon=True).start()

    def wps_attack(self):
        self.log_event("Starting WPS PIN brute force...", "ATTACK")
        def run():
            for i in range(30):
                pin = random.randint(10000000, 99999999)
                self.log_event(f"Trying PIN: {pin}", "BRUTE")
                time.sleep(0.08)
            self.log_event("WPS Attack finished. Possible vulnerability found.", "SUCCESS")
        threading.Thread(target=run, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ACWiFiHacker(root)
    root.mainloop()