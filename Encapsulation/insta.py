

class InstagramAccount:

    def __init__(self,account_name,password):
        self.account_name=account_name
        self._private_reels=[]
        self.__archived_reels=[]
        self.__password=password

    def add_private_reel(self,reel_name):
        self._private_reels.append(reel_name)
        print(f"{reel_name} added to private reel ")

    def display_private_reels(self,is_follower):
        if is_follower:
            print(f"the private reels is {self._private_reels}")
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self,reel_name):
        self.__archived_reels.append(reel_name)
        print(f"{reel_name} added to archive reel")

    def display_archived_reel(self,password):
        if password==self.__password:
            print(f"archived reels are.{self.__archived_reels}")
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self,password):
        if password==self.__password:
            return self.__archived_reels
        else:
            print("access dedained") 

    def set_update_password(self,old_password,new_password):
        if old_password==self.__password:
            self.__password=new_password  
            print("password updated successfully:")
        else:
            print("can't modifie the password:")  


account=InstagramAccount("rohith","12345")
account.add_private_reel("jooly with friends")

account.add_private_reel("madikeri trip")

account.add_archived_reel("sslc memories")

account.add_archived_reel("college days")

print("\n---private reel for (followers)---")
account.display_private_reels(True)

print("\n---private reel for (non-followers)---")
account.display_private_reels(False)

print("\n---archived reel for correct password---")
account.display_archived_reel("12345")

print("\n---archived reel for wrong password---")
account.display_archived_reel(2345)

print("\n-----updated password-----")
account.set_update_password("12345","9876")

print("\n---archived reel after updated password---")
account.display_archived_reel("9876")


