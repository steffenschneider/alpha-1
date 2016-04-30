#!/usr/bin/env python3
# coding: utf-8

import svgwrite


dokument = svgwrite.Drawing(filename="ampel.svg", size=('210mm', '297mm'))
dokument.viewbox(width=210, height=297)

# Schaft
dokument.add(dokument.line(start=(210/2, 297*4/8), end=(210/2, 297*15/16), stroke='black', stroke_width='10'))

# Körper
dokument.add(dokument.rect(insert=(210*4/10, 297*1/8), size=(210/10*2, 297/8*3), rx=1/2, ry=1/2, fill='black'))

# Lampen
dokument.add(dokument.circle(center=(210/2, ((297*3/16)+5)), r=210/17, fill='red'))
dokument.add(dokument.circle(center=(210/2, 297*5/16), r=210/17, fill='orange'))
dokument.add(dokument.circle(center=(210/2, ((297*7/16)-5)), r=210/17, fill='green'))

# Dach
dokument.add(dokument.polygon(points=[(210*3.8/10, 297*1.01/8), (210/2, 297*3.04/32), (210*6.2/10, 297*1.01/8), (210*6.2/10,297*1.08/8), (210*3.8/10, 297*1.08/8)], fill='black'))


dokument.save()
