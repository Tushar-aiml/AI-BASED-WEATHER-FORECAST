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

    @alice.on_interval(period=3.0)
    async def send_message(ctx: Context):
        await ctx.send(bob.address, Message(message="where are you from ?"))

    @alice.on_message(model=Message)
    async def alice_message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info(f"Received message from {sender}: {msg.message}")

    # Define behaviors for Bob
    @bob.on_message(model=Message)
    async def bob_message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info(f"Received message from {sender}: {msg.message}")
        await ctx.send(alice.address, Message(message="i'm from agentverse")) 
    
    @alice.on_interval(period=3.0)
    async def send_message(ctx: Context):
        await ctx.send(bob.address, Message(message="ohh nice , i'm also from there."))

    @alice.on_message(model=Message)
    async def alice_message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info(f"Received message from {sender}: {msg.message}")

    # Define behaviors for Bob
    @bob.on_message(model=Message)
    async def bob_message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info(f"Received message from {sender}: {msg.message}")
        await ctx.send(alice.address, Message(message="would you be my friend"))  

    @alice.on_interval(period=3.0)
    async def send_message(ctx: Context):
        await ctx.send(bob.address, Message(message="ofcourse!"))

    @alice.on_message(model=Message)
    async def alice_message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info(f"Received message from {sender}: {msg.message}")

    # Define behaviors for Bob
    @bob.on_message(model=Message)
    async def bob_message_handler(ctx: Context, sender: str, msg: Message):
        ctx.logger.info(f"Received message from {sender}: {msg.message}")
        await ctx.send(alice.address, Message(message=str(input(""))))

        if sender =='agent1q2jdep90pnjjzn0dnle2726c95ff7guh3ru7p7fz50zzfl5y0p00w':
            await ctx.send(sender,Request(message=""))
    # Create a bureau, add agents, and run
    bureau = Bureau()
    bureau.add(alice)
    bureau.add(bob)
    bureau.run() 
