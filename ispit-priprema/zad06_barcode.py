'''
6. Barcode Generator
The equipment in a Christmas decoration shop has broken down. Items that contain even numbers in their barcode cannot be marked by the cashiers. Your task is to write a program that generates all barcodes that do NOT contain even numbers.
Input Data
Two four-digit numbers, which show the range of the barcodes, which you’ll need to change.
    • First line – a four-digit number – the start of the range. Integer in the range [1000…9999]
    • Second line – a four-digit number – end of the range. Integer in the range [1000…9999]
Output Data
All "barcodes" that do NOT contain an even number, separated by a space, must be printed on the console. 
'''
prvi_br = input()
drugi_br = input()

# prvi_br[0] = "1"
for pc in range(int(prvi_br[0]), int(drugi_br[0]) + 1):
    for dc in range(int(prvi_br[1]), int(drugi_br[1]) + 1):
        for tc in range(int(prvi_br[2]), int(drugi_br[2]) + 1):
            for cc in range(int(prvi_br[3]), int(drugi_br[3]) + 1):
                if(pc%2 !=0 and dc%2 != 0 and tc%2 !=0 and cc%2 !=0):
                    print(f"{pc}{dc}{tc}{cc}", end = " ")