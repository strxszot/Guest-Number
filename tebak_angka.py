#!/usr/bin/env python3
import random

def main():
    print("🎯 Tebak Angka — lvcyfer (Terminal)")
    try:
        min_val = int(input("Masukkan batas bawah (contoh 1): "))
    except ValueError:
        min_val = 1
    try:
        max_val = int(input("Masukkan batas atas (contoh 100): "))
    except ValueError:
        max_val = 100
    try:
        max_tries = int(input("Masukkan jumlah kesempatan (contoh 10): "))
    except ValueError:
        max_tries = 10

    if max_val <= min_val:
        print("Nilai max harus lebih besar dari min. Menggunakan default 1-100.")
        min_val, max_val = 1, 100

    secret = random.randint(min_val, max_val)
    tries_left = max_tries
    guesses = []

    print(f"Ok! Aku sudah memilih angka antara {min_val} dan {max_val}. Kamu punya {max_tries} kesempatan. Good luck!\n")

    while tries_left > 0:
        try:
            guess = int(input(f"Tebakan kamu ({tries_left} kesempatan tersisa): "))
        except ValueError:
            print("⚠️ Masukkan hanya angka!
")
            continue

        if guess in guesses:
            print("Kamu sudah menebak angka ini sebelumnya. Coba angka lain.\n")
            continue
        guesses.append(guess)

        tries_left -= 1

        if guess == secret:
            print(f"🎉 BENAR! Kamu menebak dengan tepat! Angka: {secret}")
            print(f"Kamu berhasil dalam {max_tries - tries_left} percobaan.\n")
            break
        elif guess < secret:
            print("📉 Terlalu kecil!\n")
        else:
            print("📈 Terlalu besar!\n")

        if tries_left <= 0:
            print(f"💀 Kesempatan habis. Angka rahasianya adalah {secret}.\n")

    print("Riwayat tebakan:", guesses)
    print("Terima kasih sudah bermain 🙌")

if __name__ == '__main__':
    main()
