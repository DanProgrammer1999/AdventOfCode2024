def format_input(input):
  input = input.strip()
  rules, page_updates = input.split('\n\n')
  rules = rules.split('\n')
  page_updates = page_updates.split('\n')

  page_updates = [pages.split(',') for pages in page_updates]

  return rules, page_updates

def build_rules_dict(rules):
  rules_dict = {}

  for rule in rules:
    left, right = rule.split('|')

    if left not in rules_dict:
      rules_dict[left] = set()

    rules_dict[left].add(right)

  return rules_dict  

def validate_pages_follow_rules(pages, rules: dict[str, set[str]]):
  printed_pages = set()
  
  for page in pages:
    if page in rules and rules[page].intersection(printed_pages):
      return False
    
    printed_pages.add(page)

  return True

def page_ranking(page, page_set, rules_dict):
  return len(rules_dict[page].intersection(page_set))

def fix_pages(pages, rules: dict[str, set[str]]):
  page_set = set(pages)
  return sorted(pages, key=lambda page: page_ranking(page, page_set, rules), reverse=True)

def part1(input):
  rules, page_updates = format_input(input)

  rules_dict = build_rules_dict(rules)

  res = 0

  for pages in page_updates:
    if validate_pages_follow_rules(pages, rules_dict):
      new = int(pages[(len(pages) - 1) // 2])
      res += new

  return res


def part2(input):
  rules, page_updates = format_input(input)

  rules_dict = build_rules_dict(rules)

  res = 0

  for pages in page_updates:
    if not validate_pages_follow_rules(pages, rules_dict):
      pages = fix_pages(pages, rules_dict)
      res += int(pages[(len(pages) - 1) // 2])

  return res

