a = {}

a["이름"] = "전재병"
a["나이"] = "25살"
a["학번"] = "2019xxxxxx"
a["학과"] = "응용통계학과"
a["생일"] = "19981208"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학번"]
del a["학과"]
del a["생일"]

print(a)
print(len(a))
print()

a = dict(이름 = "전재병", 나이 = "25살", 학번 = "2019xxxxxx", 학과 = "응용통계학과", 생일 = "19981208")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))