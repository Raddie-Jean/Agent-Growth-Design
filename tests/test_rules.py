import unittest,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/"scripts"))
from validate_rules import validate,Ledger
class Rules(unittest.TestCase):
 def test_all_products(self):
  for p in (R/"fixtures").glob("*.json"):
   with self.subTest(product=p.stem):
    c=json.loads(p.read_text());self.assertTrue(validate(c));l=Ledger(c)
    self.assertEqual(l.claim("day-1",1,False),0)
    with self.assertRaises(ValueError):l.claim("day-2",1,True)
    for t in c["tasks"]:
     self.assertEqual(l.claim(t["id"],t["day"],True),t["reward"])
     self.assertEqual(l.claim(t["id"],t["day"],True),0)
    self.assertEqual(l.summary(),c["total"]);self.assertEqual(l.summary(),c["total"])
 def test_corrupt_total(self):
  c=json.loads((R/"fixtures/open-design.json").read_text());c["total"]+=1
  with self.assertRaises(AssertionError):validate(c)
 def test_duplicate_id(self):
  c=json.loads((R/"fixtures/open-design.json").read_text());c["tasks"][1]["id"]="day-1"
  with self.assertRaises(AssertionError):validate(c)
if __name__=="__main__": unittest.main()
