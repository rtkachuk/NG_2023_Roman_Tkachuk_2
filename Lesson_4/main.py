from rich.console import Console
from rich.json import JSON
import time

console = Console()

console.log("Hello")
console.log(JSON('["foo", "bar"]'))
console.rule("[bold red]Kek, here be dragons")

with console.status("Looping..."):
    for index in range(0,3):
        console.log(index)
        time.sleep(1)