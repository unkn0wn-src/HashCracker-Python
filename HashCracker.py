import hashlib, sys

def crack_hash(file, hash, hash_alg):
    PWD_FILE = open(file)
    
    for line in PWD_FILE.readlines():

        pwd = line.strip('\n')

        if hash_alg == "sha1":
            pwd_hash = hashlib.sha1(str.encode(pwd))
        elif hash_alg == "sha256":
            pwd_hash = hashlib.sha256(str.encode(pwd))
        elif hash_alg == "sha512":
            pwd_hash = hashlib.sha512(str.encode(pwd))
        elif hash_alg == "md5":
            pwd_hash = hashlib.md5(str.encode(pwd))
        else:
            print("[-] Just use one of the given algorithm")
            break

        if hash == pwd_hash.hexdigest():
            print("[!] PASSWORD FOUND")
            print("[+] The password for your hash is: " + pwd)
            break

if __name__ == "__main__":
    if len(sys.argv) == 4:
        crack_hash(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python3 HashCracker.py [Passwords File] [Hash] [sha1 sha256 sha512 md5]")
