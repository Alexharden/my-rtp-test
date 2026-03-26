import random
import sys

def simulate_rtp(total_spins, target_rtp=90.0):
    bet_per_spin = 10
    total_bet = 0
    total_win = 0
    
    for _ in range(total_spins):
        total_bet += bet_per_spin
        if random.randint(1, 100) <= 10: # 10% 中獎率
            total_win += 90 # 中獎拿 90
            
    actual_rtp = (total_win / total_bet) * 100
    print(f"模擬次數: {total_spins}, 目標 RTP: {target_rtp}%, 實際 RTP: {actual_rtp:.2f}%")
    
    # 如果偏差超過 1%，我們就判定測試失敗 (Bug)
    if abs(actual_rtp - target_rtp) > 1.0:
        print("❌ 測試失敗：RTP 偏差過大！")
        sys.exit(1) # 回傳錯誤代碼，讓 CI 變紅燈
    else:
        print("✅ 測試通過：RTP 在正常範圍內。")
        sys.exit(0)

if __name__ == "__main__":
    simulate_rtp(1000000) # 跑 100 萬次
    with open("test_report.txt", "w") as f:
        f.write(f"Actual RTP: {actual_rtp:.2f}%")
