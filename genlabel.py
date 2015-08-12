import qrcode
import argparse
import re
import base64
import StringIO

parser = argparse.ArgumentParser(description='Generate QR code for hacman.')
parser.add_argument('--name', '-n', required=True, help='Equipment Name')
parser.add_argument('--source', '-s', required=True, help='Equipment Source')
parser.add_argument('--url', '-u', required=True, help='Equipment Wiki URL')
parser.add_argument('--requires-induction', '-i', action='store_true', help='Equipment Requires Induction')
args = parser.parse_args()

f = open('EquipmentTemplate.svg', 'r')
template = f.read()
f.close()

output = re.sub(r'{EQUIP_NAME}', args.name, template)
output = re.sub(r'{EQUIP_SOURCE}', args.source, output)
output = re.sub(r'{EQUIP_URL}', args.url, output)
if args.requires_induction:
    output = re.sub(r'{EQUIP_INDUCTION}', 'REQUIRES INDUCTION', output)
else:
    output = re.sub(r'{EQUIP_INDUCTION}', ' ', output)

img = qrcode.make(args.url)

out = StringIO.StringIO()
img.save(out, 'PNG')
output = re.sub(r'{EQUIP_QR}', base64.b64encode(out.getvalue()), output)
out.close()

outFile = open("%s.svg" % args.name, 'w')
outFile.write(output)
outFile.close()
