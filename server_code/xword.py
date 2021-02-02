import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server

file = str(app_files.words.get_bytes(), 'UTF-8')
#print(type(file))
file = file.split()
#words = {line.strip("\n").strip("'s").lower() for line in file}
words = {line.strip("\n").replace("'s",'').lower() for line in file}
#print(type(words)) 
words = sorted(words)[1:]  # Ignore the empty word at the start of the list.
#print(words)

@anvil.server.callable
def find_possible_matches(pattern):
    """Given any pattern of the type "__a___b__c", this function
       looks up and returns all the potential matches for the
       pattern in the Linux dictionary of words."""

    def match_pattern(w, p):
        """Returns True if 'w' matches 'p', False otherwise."""
        letters = {k: v for k, v in enumerate(p) if v != "_"}
        return not any([w[i] != p[i] for i in letters.keys()])

    pattern = pattern.lower()  # Just in case...
    matches = [
        word  ## SELECT...
        for word in words  ## FROM...
        if len(word) == len(pattern) and match_pattern(word, pattern)  ## WHERE...
        ]
    return matches
  
  
@anvil.server.http_endpoint('/pattern/:pat')
def find_matches(pat, **q):
  result = find_possible_matches(pat)
  return result
