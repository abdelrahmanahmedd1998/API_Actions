import os
import sys
import xml.etree.ElementTree as ET

path, title = sys.argv[1], sys.argv[2]

if not os.path.exists(path):
    print(f"### {title}\n:warning: No results file found. Tests may have crashed before running.")
    sys.exit(0)

root = ET.parse(path).getroot()
suites = [root] if root.tag == "testsuite" else root.findall("testsuite")

total = sum(int(s.get("tests", 0)) for s in suites)
failures = sum(int(s.get("failures", 0)) for s in suites)
errors = sum(int(s.get("errors", 0)) for s in suites)
skipped = sum(int(s.get("skipped", 0)) for s in suites)
passed = total - failures - errors - skipped

icon = ":white_check_mark:" if failures + errors == 0 else ":x:"
print(f"### {icon} {title}\n")
print("| Total | Passed | Failed | Errors | Skipped |")
print("|---|---|---|---|---|")
print(f"| {total} | {passed} | {failures} | {errors} | {skipped} |")

failed = [
    f"- `{tc.get('classname')}::{tc.get('name')}`"
    for s in suites
    for tc in s.iter("testcase")
    if tc.find("failure") is not None or tc.find("error") is not None
]
if failed:
    print("\n**Failed tests:**")
    print("\n".join(failed))