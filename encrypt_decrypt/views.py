from django.shortcuts import render


def homepage(request):
    return render(request, 'login_user.html')

def encrypt_decrypt(request):
    def encryption(text):
        #uses caesar cipher
            alphabets = "abcdefghijklmnopqrstuvwxyz!#$%&()*+-/:;<=>?@[]^_{|}~0123456789"
            text_input = text
            shifts = 3
            encrypt_mssg = ''
            for i in range(len(text_input)):
                if text_input[i] not in alphabets:
                    encrypt_mssg += text_input[i]
                for j in range(len(alphabets)):
                    if text_input[i] in alphabets[j]:
                        encrypt_mssg += alphabets[(j + shifts) % 26]
            return encrypt_mssg

    def decryption(text):
        # uses caesar cipher
        alphabets = "abcdefghijklmnopqrstuvwxyz!#$%&()*+-/:;<=>?@[]^_{|}~0123456789"
        d_text = text
        shifts = 3
        decrypt_mssg = ''
        for i in range(len(d_text)):
            if d_text[i] not in alphabets:
                decrypt_mssg += d_text[i]
            for j in range(len(alphabets)):
                if d_text[i] in alphabets[j]:
                    decrypt_mssg += alphabets[(j - shifts) % 26]
        return decrypt_mssg

    if request.method == 'POST':
        text = request.POST.get('text')
        btn_encrypt = request.POST.get('btn_encrypt')
        btn_decrypt = request.POST.get('btn_decrypt')

        if btn_encrypt:
            n = encryption(text)
            param = {'result': n, 'btn': 'Encrypted'}

        if btn_decrypt:
            n = decryption(text)
            param = {'result': n, 'btn': 'Decrypted'}

    return render(request, 'result.html', param)

