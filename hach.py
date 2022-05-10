import hashlib

print("algorithms_available : sha512 ,sha256,sha1,md5")
print('-----------------------------------------------')
print('-----------------------------------------------')
print('')
hach=input('put your hash : ')
print('')
shous=input('choose the type of encryption :  ')
fil=open('list_hash.txt','r')
for i in fil:
    text=i.split()[0]
    if shous == "md5":
        encod=hashlib.md5(text.encode())
        has=encod.hexdigest()
        if has==hach:
            print(f'your hach is :{text}')
            break;
    if shous == "sha1":
        encod=hashlib.sha1(text.encode())
        has=encod.hexdigest()
        if has==hach:

            print(f'your hach is :{text}')
            break;   
    if shous == "sha512":
        encod=hashlib.sha512(text.encode())
        has=encod.hexdigest()
        if has==hach:
            print(f'your hach is :{text}')
            break;   
    if shous == "sha256":
        encod=hashlib.sha256(text.encode())
        has=encod.hexdigest()
        if has==hach:
            print(f'your hach is :{text}')
            break;  
    else:
        print('Sorry, the encryption cannot be broken') 
        break;   
fil.close()
print("your search compolet *_*")