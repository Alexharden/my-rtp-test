import random
import sys

def simulate_rtp(total_spins, target_rtp=90.0):
    bet_per_spin = 10
    total_bet = 0
    total_win = 0
    for _ in range(total_spins):
        total_bet += bet_per_spin
        if random.randint(1, 100) <= 10:
            total_win += 90 
    actual_rtp = (total_win / total_bet) * 100
    print(f"模擬次數: {total_spins}, 目標 RTP: {target_rtp}%, 實際 RTP: {actual_rtp:.2f}%")

    return actual_rtp

if __name__ == "__main__":
    target = 90.0
    # 1. 先跑測試
    print("正在執行模擬...")
    res_rtp = simulate_rtp(1000000, target)
    
    # 2. 【關鍵】先寫入檔案，確保檔案一定會產生
    print(f"實際 RTP: {res_rtp:.2f}%。正在寫入報告...")
    with open("test_report.txt", "w") as f:
        f.write(f"Actual RTP: {res_rtp:.2f}%")
    
    # 3. 最後才判斷 Exit Code
    if abs(res_rtp - target) <= 1.0:
        print("✅ 測試通過")
        sys.exit(0)
    else:
        print("❌ 測試失敗")
        sys.exit(1)
