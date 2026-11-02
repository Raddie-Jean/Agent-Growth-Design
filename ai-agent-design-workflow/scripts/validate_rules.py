import json,sys
def validate(c):
    ts=c["tasks"]
    assert len({t["id"] for t in ts})==len(ts), "duplicate task"
    assert all(isinstance(t["reward"],int) and t["reward"]>=0 for t in ts)
    assert sum(t["reward"] for t in ts)==c["total"], "reward total mismatch"
    assert not c["summary_grants_reward"], "double grant"
    assert all(t["completion"] for t in ts)
    assert {t["day"] for t in ts}==set(range(1,max(t["day"] for t in ts)+1))
    return True
class Ledger:
    def __init__(self,c):
        validate(c);self.c=c;self.claimed=set();self.balance=0
    def claim(self,task_id,day,accepted=False):
        t=next(t for t in self.c["tasks"] if t["id"]==task_id)
        if t["day"]>day: raise ValueError("locked")
        if not accepted: return 0
        if task_id in self.claimed: return 0
        self.claimed.add(task_id);self.balance+=t["reward"];return t["reward"]
    def summary(self): return self.balance
if __name__=="__main__":
    c=json.load(open(sys.argv[1]));validate(c);print(c["product"],"PASS",c["total"])
