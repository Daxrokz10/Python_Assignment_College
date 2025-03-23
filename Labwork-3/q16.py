# 16. Mask Credit Card Number

def mask_credit_card_number(credit_card_number):
    masked_credit_card_number = '*' * 12 + credit_card_number[-4:]
    return masked_credit_card_number

credit_card_number = input("Enter a credit card number: ")
masked_credit_card_number = mask_credit_card_number(credit_card_number)
print("Masked credit card number:", masked_credit_card_number)