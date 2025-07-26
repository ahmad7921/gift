print("ko")


import json 
import argparse as ap
import os
from datetime import datetime 


import pandas as pd


EXP_FILE = "expense.json"

def load_exp ():
    if not os.path.exists(EXP_FILE):
        return []
    with open(EXP_FILE, "r") as f:
        try :
            return json.load(f)
        except json.JSONDecodeError :
            return []
        
def save_exp (exp):
    with open(EXP_FILE, "w") as f :
        json.dump(exp, f, indent=4)



def add_exp (description , amount ) :
    exp = load_exp()
    id = max ([e["id"] for e in exp ], default= 0) + 1
    now = datetime.now().isoformat()

    new_exp = {
        "id" : id , 
        "description" : description , 
        "amount" : amount ,
        "created_date" : now , 
        "dupdated_date" : now
    }
    exp.append(new_exp)
    save_exp(exp)
    print(f"Expense added successfully (ID: {id})")


def del_exp (id):
    exp = load_exp()
    new_exp = [e for e in exp if e['id'] != id]
    if len (exp) == len(new_exp) :
        print(f"there is no ID like that ({id})")
    else :
        save_exp(new_exp)
        print("Expense deleted successfully ")


def upd_exp (id ,  amount):
    rong_id = True
    exp = load_exp()
    for e in exp :
        if e["id"] == id :
            old_exp = e
            rong_id = False
            break
    if rong_id == False :
        now = datetime.now().isoformat()
        new_exp = {
            "id" : id , 
            "description" : old_exp["description"] , 
            "amount" : amount ,
            "created_date" : old_exp["created_date"] , 
            "updated_date" : now
        }
        final_exp = [e for e in exp if e["id"] != id]
        final_exp.append(new_exp)
        save_exp(final_exp)
        print(f"Expense updated successfully (ID: {id})")
    else :
        print(f"incorrect ID -> {id}")

    
def list_exp () :
    exp = load_exp()
    pd_exp = pd.DataFrame(exp)
    pd_exp["created_date"] = pd_exp["created_date"].str[:10]
    print(pd_exp[["id" , "description" , "amount" ,"created_date" ]])
    
    
def sum_exp (): 
    exp = load_exp()
    total = 0
    for e in exp :
        total = total + e["amount"]
    print(f"Total expense : {total} ")

p = ap.ArgumentParser(description="<<-- Expense tracker -->>")
subp = p.add_subparsers(dest= "command")

add = subp.add_parser( "add")
add.add_argument ( "description" , type= str , help="description of the expense")
add.add_argument( "amount" , type= float , help= "amount of the expenses")

delete = subp.add_parser("delete")
delete.add_argument("id" , type= int  , help= " ID of the expense")

update = subp.add_parser("update")
update.add_argument("id" , type= int  , help= " ID of the expense")
update.add_argument( "amount" , type= float , help= "amount of the expenses")

exp_list = subp.add_parser("list")

exp_sum = subp.add_parser("sum")

args = p.parse_args()
print(args)
if args.command == "add" :
    add_exp(args.description ,args.amount)


if args.command == "delete" :
    del_exp(args.id)

if args.command == "update" :    
    upd_exp(args.id ,  args.amount )

if args.command == "list" :
    list_exp()

if args.command == "sum" :
    sum_exp()


    