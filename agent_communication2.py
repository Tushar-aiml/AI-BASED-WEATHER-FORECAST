# Import necessary classes from uagents module
from uagents import Agent, Bureau, Context, Model

class Message(Model):
    message: str

if __name__ == "__main__":
    # Define agents and behaviors within the main block
    alice = Agent(name="alice")
    bob = Agent(name="bob")

    # Define behaviors for Alice
    @alice.on_interval(period=3.0)
    async def send_message(ctx: Context):
        await ctx.send(bob.address, Message(message="hello there bob"))

    @alice.on_message(model=Message)
    async def alice_message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info(f"Received message from {sender}: {msg.message}")

    # Define behaviors for Bob
    @bob.on_message(model=Message)
    async def bob_message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info(f"Received message from {sender}: {msg.message}")
        await ctx.send(alice.address, Message(message="hello there alice"))
        

    # Create a bureau, add agents, and run
    bureau = Bureau()
    bureau.add(alice)
    bureau.add(bob)
    bureau.run() 
