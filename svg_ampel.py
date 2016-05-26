#!/usr/bin/env python3
# coding: utf-8

import svgwrite


dokument = svgwrite.Drawing(filename="ampel.svg", size=('210mm', '297mm'))
dokument.viewbox(width=210, height=297)

dokument.add(dokument.line(start=(11, 111), end=(111, 111), stroke='black', stroke_width='1'))
dokument.add(dokument.rect(insert=(23, 28), size=(26, 38), rx=1 / 2, ry=1 / 2, fill='black'))
dokument.add(dokument.circle(center=(22, 29), r=7, fill='red'))
dokument.add(
    dokument.polygon(points=[(210 * 6.2 / 10, 297 * 1.08 / 8), (210 * 3.8 / 10, 297 * 1.08 / 8)], fill='black'))

dokument.save()
