from fastapi import FastAPI
from pydantic import BaseModel

from BlockChain import BlockChain, Transaction
from Peer import Peer


class Node(BaseModel):
    node: str


app = FastAPI()
chain = BlockChain()


@app.get("/blocks")
def get_blocks():
    return [block.as_dict() for block in chain.blocks]


@app.get("/blocks/{index}")
def get_block(index: int):
    return chain.blocks[index].as_dict()


@app.post("/blocks/mine")
def mine_block():
    block = chain.create_block()
    return block.as_dict()


@app.get("/transactions")
def get_transactions():
    return [transaction.as_dict() for transaction in chain.transactions]


@app.post("/transactions/new")
def new_transaction(transaction: dict):
    try:
        t = Transaction.from_dict(transaction)
    except ValueError:
        return {"error": "Invalid transaction"}

    return chain.add_transaction(t.sender, t.recipient, t.amount).as_dict()


@app.get("/nodes")
def get_nodes():
    return [peer.address for peer in chain.network]


@app.post("/nodes/register")
def register_node(node: "Node"):
    peer = Peer(node.node)
    chain.network.accept(peer)
    return {"message": "New node has been added"}


@app.patch("/nodes/resolve")
def resolve_conflicts():
    if chain.resolve() is True:
        return {"message": "Resolved conflicts"}
    else:
        return {"message": "No conflicts"}


@app.get("wallet/{address}/balance")
def get_balance(address: str):
    return chain.getbalance(address)


@app.get("wallet/{address}/transactions")
def get_transactions(address: str):
    return chain.gettransactions(address)
