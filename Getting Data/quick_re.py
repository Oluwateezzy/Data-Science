import re

print(re.sub(r'([LRUD])(\d+)', '***', 'Locations L3 and D22 full.'))

print(r'this is a raw string. Backlashes do not do anything special.')

print('abcdef abcxyz'.replace('abc', '**'))

print(re.sub(r'abc', '**', 'abcdef abcxyz'))

print(re.sub(r'[ad]', '**', 'abcedf'))

print(re.sub(r'[abc][123]', '**', 'a1 + b2 + c5 + x3'))

print(re.sub(r'A.B', '**', 'A2B AxB AxxB A$B'))

print(re.sub(r'AB+?', '*', 'ABC ABBBBBBC AC'))

print(re.sub(r'abc|xyz', '**', 'abcdefxyz123abc'))

print(re.sub(r'^abc', '*', 'abcdefgabc'))

print(re.sub(r'abc$', '*', 'abcdefgabc'))

print(re.sub(r'AB\+', '*', 'AB+C'))

print(re.sub(r'\d', '*', '3 + 14 = 17'))

print(re.sub(r'\D', '*', '3 + 14 = 17'))

print(re.sub(r'\w', '*', 'This is a test. Or is it?3'))

print(re.sub(r'\W', '*', 'This is a test. or is it?'))

print(re.sub(r'\s', '*', 'This is a text. Or is it?'))

print(re.sub(r'\S', '*', 'This is a test. Or is it?'))

print(re.sub(r'the(?= cat)', '*', 'the dog and the cat'))

print(re.sub(r'(?<!\w)[Tt]he(?!\w)', '*', 'The cat is on the lathe there'))

print(re.sub('(?i)ab', '*', 'ab AB'))

pattern = r"""(?x)[AB]\d+ # Match A or B followed by some digits
                [CD]\d+ # Match C or D followed by some digits
            """
pattern2 = r"""(?x)[AB]\d+ # Match A or B followed by some digits
                [CD]\d+ # Match C or D followed by some digits
            """

print(re.sub(pattern, '*', 'A3C9 and C1B17'))

print(re.sub(pattern2, '*', 'A3C9 and C1B17'))