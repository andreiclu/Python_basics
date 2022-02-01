class Encryptor:
    def encrypt(self, to_encrypt):
        pass


class BCryptEncryptor(Encryptor):
    def encrypt(self, to_encrypt):
        return f"encrypting {to_encrypt} with BCrypt"


class SCryptEncryptor(Encryptor):
    def encrypt(self, to_encrypt):
        return f"encrypting {to_encrypt} with SCrypt"


class NoOpEncryptor(Encryptor):
    def encrypt(self, to_encrypt):
        return to_encrypt


class Encryptors:
    def encrypt_without_modification(self, to_encrypt):
        pass

    def encrypt_with_bcrypt(self, to_encrypt):
        pass

    def encrypt_with_scrypt(self, to_encrypt):
        pass


class EncryptionFacade(Encryptors):
    def __init__(self, scrypt_encryptor, bcrypt_encryptor, noop_encryptor):
        self._scrypt_encryptor = scrypt_encryptor
        self._bcrypt_encryptor = bcrypt_encryptor
        self._noop_encryptor = noop_encryptor

    def encrypt_without_modification(self, to_encrypt):
        return self._noop_encryptor.encrypt(to_encrypt)

    def encrypt_with_bcrypt(self, to_encrypt):
        return self._bcrypt_encryptor.encrypt(to_encrypt)

    def encrypt_with_scrypt(self, to_encrypt):
        return self._scrypt_encryptor.encrypt(to_encrypt)


scrypt_encript = SCryptEncryptor()
bcrypt_encript = BCryptEncryptor()
noop_encript = NoOpEncryptor()
encryiption_facade = EncryptionFacade(scrypt_encript, bcrypt_encript, noop_encript)
print(encryiption_facade.encrypt_with_scrypt('la la la'))
print(encryiption_facade.encrypt_with_bcrypt('ho ho ho'))
