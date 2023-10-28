import os
import random
import string
import rich
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.progress import track
import time


console = rich.console.Console()

# Title
print(Panel('[blue]Password Generator![/blue]', style="bold"))

length = int(input('\nEnter the length of password: '))
console.print("[grey]\n--------------------------------------")
console.print("Level - 1 : [red]Weak[/red]")
console.print("Level - 2 : [yellow]Good[/yellow]")
console.print("Level - 3 : [green]Secure[/green]")

choice = int(input("\nChoose the level: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Different Options 
match choice:
    case 1:
        all = lower + upper
        
    case 2:
        all = lower + upper + num
        
    case 3:
        all = lower + upper + num + symbols
        
    case default:
        print("""Invalid Choice!
        Default Choice""")
        all= lower

os.system('cls')

# Fancy looking progress Bar
t=random.randint(0,5)
print("")
for i in track(range(t), description="[brown]Generating Password...[/brown]"):
    time.sleep(1) 
    
# Finally all Strings are joined to create the Password
temp = random.sample(all,length)
password = "".join(temp)
print("")
console.print(f"[white]{password}",style="Bold reverse")


