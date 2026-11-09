from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).resolve().parent
manifest=json.loads((root/'file_manifest.json').read_text())
for row in manifest['files']:
    p=root/row['path']
    assert p.stat().st_size==row['bytes'],row['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['path']
    if p.suffix=='.zip':
        with zipfile.ZipFile(p) as z:assert z.testzip() is None,p.name
nb=json.loads((root/'ATRS_AI_Assisted_Census.ipynb').read_text())
cells=[c for c in nb['cells'] if c['cell_type']=='code']
assert len(cells)==12 and all(c.get('execution_count') is not None for c in cells)
assert not any(o.get('output_type')=='error' for c in cells for o in c.get('outputs',[]))
assert json.loads((root/'Census_Validation.json').read_text())['passed']==34
print('PASS: release hashes, ZIP integrity and recorded execution state. This is not semantic or publication approval.')
