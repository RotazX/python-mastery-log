# Original Week 1 loop (week01/log_parser.py):
# errors = []
# for line in lines:
#     if "ERROR" in line:
#         errors.append(line.strip())

def find_errors(lines: list[str]) -> list[str]:
    return [line.strip() for line in lines if "ERROR" in line]