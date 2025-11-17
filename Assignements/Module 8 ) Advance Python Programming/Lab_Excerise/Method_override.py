class master:
    def header(self,pname):
        print(f"this is {pname}")

class home(master):
    def header(self, pname):
        return super().header(pname)
    
class about(master):
    def header(self, pname):
        return super().header(pname)
    
h = home()
h.header("home")

a = about()
a.header("about")