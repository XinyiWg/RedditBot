import pickle
x = {'ADJ-FORGET': ['forget', 'forgive', 'find an excuse to', 'ignore', 'disregard'],\
     'NUMBER': ['one', 'two', 'three', 'four', 'five', 'six', 'ten'],\
     'ADJ-FUNNY': ['hilarious', 'funny', 'interesting', 'priceless', 'humorous'], \
     'VERB': ['supporting', 'electing', 'winning','chosing','naming'], \
     'ADV-MUST': ['difinitely', 'undoutedly', 'without doubt','without any hesitate','100%'], \
     'ADJ-PEOPLE': ['promising', 'bright', 'encouraging', 'golden', 'auspicious'], \
     'ADJ-GOOD': ['good', 'excellent', 'fantastic', 'amazing', 'nice'], \
     'ADJ-QUICKLY': ['quicly', 'briskly','immediately', 'speedily', 'swiftly'], \
     'REQUIREMENT': ['responsibility', 'determinant', 'inspiration', 'accountability', 'brave'], \
     'N-FAILURE': ['failure', 'unsuccess', 'carelessness', 'inadvertence', 'delinquency'], \
     'ADJ-WORST': ['worst', ' most frightening', ' most awful', ' most horrible', 'most terrible'], \
     'ADJ-BAD': ['bad', 'incompetent', 'irresponsible', 'bad-reputational', 'notorious'], \
     'ADJ-REGRET': ['regret', 'disappointed', 'frustrated', 'desperated', 'self-condemned'], \
     'ADJ-PERFECT': ['perfect', 'stunning', 'nice', ' flawless', 'indefectible'], \
     'PHARSE': ['disaster', 'nightmare', 'apocalypse', 'calamity', 'catastrophe'], \
     'ADV-UNDOUTEDLY': ['undoutedly', 'most likely', 'probably', 'without doubt', 'difinitely'], \
     'N-DECISION': ['decision', 'choice', 'conclusion', 'resolution', 'selection'], \
     'PHARSE-LONGTIME': ['day and night', 'a long time', 'the whole week', 'the whole year', 'the whole day', 'the whole night'], \
     'ADJ-BRIGHT': ['bright', 'good', 'full of hope', 'lucky', 'glowing'], \
     'ADJ-SMART': ['smart', 'wise', 'intelligent', 'genius', 'brilliant'], \
     'ADJ-RIGHT': ['right', 'correct', 'birthright', 'proper', 'reliable'], \
     'GOODTHINGS': ['future', 'perspective', 'tomorrow', 'hope', 'a smash hit'], \
     'ADJ-HAPPY': ['happy', 'familiar', 'nice', 'convinced', 'right'], \
     'ADJ-COOL': ['cool', 'promising', 'coooool','fantastic', 'amazing']}
f = open("word_dict.pkl", "wb")
pickle.dump(x, f)
f.close() 