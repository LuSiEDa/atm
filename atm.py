# balance : 초기 잔액을 설정하는 변수를 초기화해주세요.
# 금액은 마음대로 설정.

balance = 10000

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택할 수 있도록
# 기능 입력을 받는 기능을 구현해주세요/

while True :
    num = input("사용하실 기능의 번호를 선택해주세요. (1.입금 2.출금 3.영수증 보기 4.종료) : ")
    
    if num == "4":  # 종료기능
        break 

    if num == "1":  # 입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount = int(input("입금할 금액을 입력해주세요.")) # str:5000 ->int->
        balance += deposit_amount # balance = balance + deposit_amount
        print(f'입금하신 금액은{deposit_amount} 원이고, 현재 잔액은 {balance} 원 입니다.')

    if num == "2":
        withdraw_amount = int(input("출금할 금액을 입력해주세요.")) # str:5000 ->int->
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount # balance = balance - withdraw_amount
        print(f'출금하신 금액은{withdraw_amount} 원이고, 현재 잔액은 {balance} 원 입니다.')

    if num == "3":
        pass

print(f"시스템이 종료되었습니다. 현재 잔액은 {balance}")