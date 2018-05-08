class Credential:
    #class property
    credential_list = []

    def __init__ (self, account, username, password):
        self.account = account
        self.username = username
        self.password = password
        Credential.credential_list.append({'account':self.account, 'username':self.username, 'password':self.password})

    def delete_account():
        pass
    @classmethod
    def view(cls):
        print("Existing Accounts: ")
        print("|| Account Name ||  username || password ")
        for i in cls.credential_list:
            print(f" || {i['account']} || {i['username']} || {i['password']}")

    def search_account():
        pass
    @classmethod
    def delete(cls, acc):
        for a in cls.credential_list:
            if a['account'] == acc:
                cls.credential_list.remove(a)


