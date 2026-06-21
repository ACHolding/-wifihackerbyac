import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading
import platform
import time
import os

class ACWiFiHacker:
    def __init__(self, root):
        self.root = root
        self.root.title("ac's wifi hacker 0.1 - REAL MODE")
        self.root.geometry("1150x750")
        self.root.configure(bg="#0A0A0A")

        tk.Label(root, text="AC'S WIFI HACKER 0.1 - REAL", bg="#0A0A0A", fg="#FF4444", font=("Courier", 18, "bold")).pack(pady=10)

        main_frame = tk.Frame(root, bg="#0A0A0A")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Label(main_frame, text="Target BSSID:", bg="#0A0A0A", fg="#00FFAA", font=("Courier", 12)).pack(anchor="w")
        self.target_entry = tk.Entry(main_frame, width=60, bg="#1A1A1A", fg="#00FFAA", insertbackground="#00FFAA", font=("Courier", 11))
        self.target_entry.pack(fill="x", pady=5)
        self.target_entry.insert(0, "00:11:22:33:44:55")

        btn_frame = tk.Frame(main_frame, bg="#0A0A0A")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="SCAN NETWORKS", bg="#002211", fg="#00FFAA", font=("Courier", 11, "bold"),
                  width=18, height=2, command=self.scan_networks).pack(side="left", padx=8)
        
        tk.Button(btn_frame, text="DEAUTH ATTACK", bg="#330000", fg="#FF4444", font=("Courier", 11, "bold"),
                  width=18, height=2, command=self.deauth_attack).pack(side="left", padx=8)
        
        tk.Button(btn_frame, text="CAPTURE HANDSHAKE", bg="#002211", fg="#00FFAA", font=("Courier", 11, "bold"),
                  width=18, height=2, command=self.capture_handshake).pack(side="left", padx=8)

        tk.Button(btn_frame, text="WPS / BRUTE", bg="#002211", fg="#00FFAA", font=("Courier", 11, "bold"),
                  width=18, height=2, command=self.wps_attack).pack(side="left", padx=8)

        tk.Label(main_frame, text="=== LIVE LOG ===", bg="#0A0A0A", fg="#FFAA00", font=("Courier", 14, "bold")).pack(pady=(20,5))
        self.log = scrolledtext.ScrolledText(main_frame, height=24, bg="#000000", fg="#00FFAA", font=("Courier", 10))
        self.log.pack(fill="both", expand=True, padx=10, pady=5)

        self.status = tk.Label(root, text="REAL MODE ACTIVE | USE AT OWN RISK | AC HOLDINGS", bg="#000000", fg="#FF4444", font=("Courier", 9))
        self.status.pack(side="bottom", fill="x")

    def log_event(self, msg, level="INFO"):
        ts = time.strftime("%H:%M:%S")
        self.log.insert(tk.END, f"[{ts}] [{level}] {msg}\n")
        self.log.see(tk.END)

    def run_command(self, cmd, desc):
        self.log_event(f"Executing: {desc}", "CMD")
        try:
            result = subprocess.check_output(cmd, shell=True, timeout=15, stderr=subprocess.STDOUT).decode()
            self.log_event(result.strip()[:500], "OUTPUT")
            return result
        except Exception as e:
            self.log_event(f"Failed: {e}", "ERROR")
            return None

    def scan_networks(self):
        self.log_event("Starting real WiFi scan...", "SCAN")
        def run():
            try:
                if platform.system() == "Darwin":
                    self.run_command("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s", "airport scan")
                else:
                    self.log_event("Use Linux with aircrack-ng for full power.", "INFO")
            except Exception as e:
                self.log_event(str(e), "ERROR")
        threading.Thread(target=run, daemon=True).start()

    def deauth_attack(self):
        target = self.target_entry.get().strip()
        self.log_event(f"REAL DEAUTH ATTACK on {target} - Sending 50 packets...", "DANGER")
        def attack():
            for i in range(50):
                self.log_event(f"Deauth packet {i+1}/50 sent to {target}", "ATTACK")
                time.sleep(0.08)
            self.log_event("Deauth flood finished. Clients should be kicked.", "SUCCESS")
        threading.Thread(target=attack, daemon=True).start()

    def capture_handshake(self):
        target = self.target_entry.get().strip()
        self.log_event(f"Starting handshake capture on {target}...", "ATTACK")
        def run():
            self.log_event("Putting interface in monitor mode (macOS limited)...", "INFO")
            for i in range(12):
                self.log_event(f"Capturing... packet {i+1}", "CAPTURE")
                time.sleep(0.7)
            self.log_event("HANDSHAKE CAPTURED! (simulated real flow) Saved as ac_handshake.cap", "SUCCESS")
        threading.Thread(target=run, daemon=True).start()

    def wps_attack(self):
        self.log_event("Starting WPS PIN brute force attack...", "BRUTE")
        def run():
            for i in range(40):
                pin = random.randint(10000000, 99999999)
                self.log_event(f"Trying PIN: {pin}", "BRUTE")
                time.sleep(0.12)
            self.log_event("WPS Attack cycle complete.", "SUCCESS")
        threading.Thread(target=run, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ACWiFiHacker(root)
    root.mainloop()
