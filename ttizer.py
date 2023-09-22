import subprocess
import argparse
import hashlib
import os


parser = argparse.ArgumentParser(description="Convert PDF to audio")
parser.add_argument("pdf_path", type=str, help="Path to PDF file")
parser.add_argument("-v", "--voice", type=str, help="Voice", default="Alex")
parser.add_argument("-o", "--output", type=str, help="Output file", default="out.aiff")
args = parser.parse_args()

pdf_path = args.pdf_path
os.makedirs("tmp", exist_ok=True)
tempdir = f"tmp/{hashlib.md5(pdf_path.encode()).hexdigest()}"
if not os.path.exists(tempdir):
    subprocess.run(["nougat", pdf_path, "-o", tempdir])
mmd = os.path.join(tempdir, os.listdir(tempdir)[0])
subprocess.run(["say", "-f", mmd,
                "-v", args.voice,
                "-o", args.output
                ])
