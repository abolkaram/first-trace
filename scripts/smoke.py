import json,re
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions
def compat(method=None,args=None,kwargs=None):
 out={}
 if method is not None: out["method"]=method
 if args: out["args"]=args
 if kwargs: out["kwargs"]=kwargs
 return out
contract_actions.make_calldata_object=compat
ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/"accounts.env").read_text(); KEY=re.search(r'^ACCOUNT_5_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip(); ADDRESS=json.loads((ROOT/"deployment.json").read_text())["contractAddress"]; client=create_client(chain=studionet,account=create_account(account_private_key=KEY))
def write(name,args):
 tx=client.write_contract(address=ADDRESS,function_name=name,args=args); print(name+"_tx="+str(tx),flush=True); receipt=client.wait_for_transaction_receipt(transaction_hash=tx,wait_until="finalized",retries=180,interval=5000,full_transaction=True); leaders=receipt.get("consensus_data",{}).get("leader_receipt") or []; leaders=[leaders] if isinstance(leaders,dict) else leaders; assert receipt.get("result_name")=="MAJORITY_AGREE" and any(item.get("execution_result")=="SUCCESS" for item in leaders); return str(tx)
manifest="https://raw.githubusercontent.com/abolkaram/first-trace/main/fixtures/manifest.json"; transactions={"pin":write("pin",[manifest]),"locate":write("locate",["LANTERN-PLEDGE-01"])}; final=client.read_contract(address=ADDRESS,function_name="get_trace",args=["LANTERN-PLEDGE-01"]); assert final["state"]=="FOUND" and final["first_index"]==1 and final["presence"]==[False,True,True,True]; proof={"traceId":"LANTERN-PLEDGE-01","contract":ADDRESS,"transactions":transactions,"final":final,"fixtureDisclosure":"The ordered public snapshots are repository-owner demonstration records, not independent publishers."}; (ROOT/"evidence").mkdir(exist_ok=True); (ROOT/"evidence"/"live-run.json").write_text(json.dumps(proof,indent=2)+"\n"); print(json.dumps(proof,indent=2))
