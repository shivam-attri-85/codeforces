# Filename: generate_cpp_cp_cheatsheet_pdf.py
# Requires: reportlab (pip install reportlab)

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

TITLE = "C++ CP/DSA Built-ins Cheat Sheet"
FILENAME = "cpp_cp_cheatsheet.pdf"

content = {
    "Arrays (algorithm)": [
        "sort(arr, arr+n); — ascending sort",
        "sort(arr, arr+n, greater&lt;int&gt;()); — descending sort",
        "binary_search(arr, arr+n, key); — exists in sorted? bool",
        "lower_bound(arr, arr+n, key); — first ≥ key (iterator)",
        "upper_bound(arr, arr+n, key); — first &gt; key (iterator)",
        "fill(arr, arr+n, val); — fill range",
        "reverse(arr, arr+n); — reverse range",
        "next_permutation(arr, arr+n); — next lexicographic permutation",
        "prev_permutation(arr, arr+n); — previous lexicographic permutation",
        "count(arr, arr+n, val); — count occurrences",
        "unique(arr, arr+n); — remove consecutive dups (returns new end)"
    ],
    "Vector (vector, algorithm)": [
        "v.push_back(x);, v.pop_back();",
        "v.size();, v.empty();, v.clear();",
        "v.front();, v.back();",
        "v.insert(v.begin()+i, x);, v.erase(v.begin()+i);",
        "sort(v.begin(), v.end());",
        "reverse(v.begin(), v.end());",
        "lower_bound(v.begin(), v.end(), key);",
        "upper_bound(v.begin(), v.end(), key);",
        "v.assign(n, val); — resize and fill",
        "v.resize(n);, v.reserve(cap);"
    ],
    "String (string, algorithm)": [
        "s.size() / s.length();",
        "s.substr(pos, len);",
        "s.find(sub);, s.rfind(sub);",
        "s.replace(pos, len, str);",
        "s.insert(pos, str);, s.erase(pos, len);",
        "s.push_back(ch);, s.pop_back();",
        "transform(s.begin(), s.end(), s.begin(), ::tolower);",
        "transform(s.begin(), s.end(), s.begin(), ::toupper);",
        "stoi(s), stol(s), stoll(s), stoull(s);",
        "to_string(x);"
    ],
    "Deque (deque)": [
        "dq.push_front(x);, dq.push_back(x);",
        "dq.pop_front();, dq.pop_back();",
        "dq.front();, dq.back();",
        "dq.size();, dq.empty();, dq.clear();"
    ],
    "Priority Queue (queue)": [
        "priority_queue&lt;int&gt; pq; — max-heap",
        "priority_queue&lt;int, vector&lt;int&gt;, greater&lt;int&gt;&gt; pq; — min-heap",
        "pq.push(x);, pq.pop();, pq.top();",
        "pq.size();, pq.empty();"
    ],
    "Set/Multiset (set, multiset)": [
        "s.insert(x);, s.erase(x or it);",
        "s.find(x);, s.count(x);",
        "s.lower_bound(x);, s.upper_bound(x);",
        "s.size();, s.empty();, s.clear();",
        "multiset allows duplicates; erase(value) removes all equal"
    ],
    "Unordered Set (unordered_set)": [
        "us.insert(x);, us.erase(x);",
        "us.find(x);, us.count(x);",
        "Average O(1) ops, no ordering"
    ],
    "Map (map)": [
        "m[key] = val;, m.insert({k,v});",
        "m.erase(key or it);",
        "m.find(key);, m.count(key);",
        "m.lower_bound(key);, m.upper_bound(key);",
        "Ordered by key (log n), iterates in sorted order"
    ],
    "Unordered Map (unordered_map)": [
        "um[key] = val;, um.insert({k,v});",
        "um.erase(key);, um.find(key);, um.count(key);",
        "Average O(1), no ordering; good for freq maps/hashmaps"
    ],
    "Math (cmath, algorithm, numeric)": [
        "abs(x);, max(a,b);, min(a,b);, swap(a,b);",
        "pow(a,b);, sqrt(x);, cbrt(x);",
        "log(x);, log10(x);, ceil(x);, floor(x);, round(x);",
        "gcd(a,b); in &lt;numeric&gt; (C++17+), lcm(a,b);",
        "accumulate(first, last, init); in &lt;numeric&gt;"
    ],
    "Bit Ops (bit, limits)": [
        "__builtin_popcount(x); (int), __builtin_popcountll(x);",
        "__builtin_ctz(x); trailing zeros, __builtin_clz(x); leading zeros",
        "bitset&lt;N&gt; b; for fixed-size bit operations",
        "INT_MAX, LLONG_MAX in &lt;climits&gt;"
    ],
    "I/O (fast)": [
        "ios::sync_with_stdio(false); cin.tie(nullptr);",
        "Use '\n' for fast newline, avoid mixing scanf/printf with iostreams"
    ],
    "Permutations/Combinatorics (algorithm)": [
        "next_permutation(v.begin(), v.end());",
        "prev_permutation(v.begin(), v.end());",
        "Generate all permutations by sorting then looping next_permutation"
    ],
    "Useful Patterns": [
        "Sort + unique to deduplicate vector: sort(v.begin(),v.end()); v.erase(unique(v.begin(),v.end()), v.end());",
        "Binary search on answer: use while(l&lt;r) with predicate on mid",
        "Two-pointer pattern for sorted arrays/ranges"
    ]
}

def build_story(styles):
    story = []

    # Use Segoe UI for general text and Consolas for code (registered in main)
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='SegoeUI-Bold' if 'SegoeUI-Bold' in pdfmetrics.getRegisteredFontNames() else 'SegoeUI',
        fontSize=20,
        leading=24,
        alignment=1,
        spaceAfter=12
    )
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='SegoeUI',
        fontSize=10,
        textColor=colors.grey,
        alignment=1,
        spaceAfter=18
    )
    h_style = ParagraphStyle(
        'Header',
        parent=styles['Heading2'],
        fontName='SegoeUI-Bold' if 'SegoeUI-Bold' in pdfmetrics.getRegisteredFontNames() else 'SegoeUI',
        fontSize=13,
        textColor=colors.HexColor("#1f4e79"),
        spaceBefore=8,
        spaceAfter=6
    )
    bullet_style = ParagraphStyle(
        'Bullets',
        parent=styles['Code'],
        fontName='Consolas' if 'Consolas' in pdfmetrics.getRegisteredFontNames() else 'Courier',
        fontSize=9.5,
        leading=12,
        leftIndent=10,
        spaceAfter=2
    )
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontName='Consolas' if 'Consolas' in pdfmetrics.getRegisteredFontNames() else 'Courier',
        fontSize=9.5,
        leading=12,
        backColor=colors.whitesmoke,
        leftIndent=6,
        rightIndent=6,
        spaceBefore=4,
        spaceAfter=4
    )

    # Title page
    story.append(Paragraph(TITLE, title_style))
    story.append(Paragraph("Competitive Programming reference for C++ STL and built-ins", subtitle_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Author: Generated by script", subtitle_style))
    story.append(Spacer(1, 40))
    story.append(Paragraph("Quick Tips:", h_style))
    story.append(Paragraph("- Use -O2 for contests. - Prefer contiguous containers for cache locality.", bullet_style))
    story.append(Spacer(1, 20))
    story.append(PageBreak())

    # Simple contents page (manual list)
    story.append(Paragraph("Contents", title_style))
    contents_lines = [f"{i+1}. {s}" for i, s in enumerate(content.keys())]
    for line in contents_lines:
        story.append(Paragraph(line, bullet_style))
    story.append(PageBreak())

    for section, lines in content.items():
        story.append(Paragraph(section, h_style))
        for line in lines:
            story.append(Paragraph("• " + line, bullet_style))
        story.append(Spacer(1, 4))

    # Quick header table of common headers
    story.append(Spacer(1, 8))
    story.append(Paragraph("Common Headers", h_style))
    table_data = [
        ["<algorithm>", "sort, reverse, lower_bound, upper_bound, next_permutation"],
        ["<vector>", "std::vector"],
        ["<string>", "std::string"],
        ["<deque>", "std::deque"],
        ["<queue>", "std::priority_queue, std::queue"],
        ["<set>, <unordered_set>", "std::set, std::multiset, std::unordered_set"],
        ["<map>, <unordered_map>", "std::map, std::multimap, std::unordered_map"],
        ["<numeric>", "accumulate, gcd, lcm"],
        ["<cmath>", "sqrt, pow, ceil, floor, log"],
        ["<bitset>", "std::bitset"],
        ["<climits>, <limits>", "INT_MAX, LLONG_MAX, numeric_limits<T>"]
    ]
    t = Table(table_data, colWidths=[4.5*cm, 11*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.25, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.whitesmoke, colors.lightyellow])
    ]))
    story.append(t)

    story.append(Spacer(1, 10))
    story.append(Paragraph("Notes", h_style))
    story.append(Paragraph("Prefer contiguous containers (vector) for cache efficiency; use reserve to avoid reallocations.", bullet_style))
    story.append(Paragraph("Choose ordered vs unordered maps/sets based on need for ordering and typical operation count.", bullet_style))
    story.append(Paragraph("For numeric heavy loops, consider -O2/-O3 and fast I/O setup.", bullet_style))

    # Resources page
    story.append(PageBreak())
    story.append(Paragraph("Resources", title_style))
    res_style = ParagraphStyle('Res', parent=styles['Normal'], fontName='SegoeUI', fontSize=10, leftIndent=6, spaceAfter=6)
    story.append(Paragraph('<a href="https://en.cppreference.com/">cppreference.com</a> - Comprehensive reference', res_style))
    story.append(Paragraph('<a href="https://codeforces.com/">Codeforces</a> - Practice & contests', res_style))
    story.append(Paragraph('<a href="https://cses.fi/">CSES</a> - Practice problems', res_style))
    story.append(Paragraph('Font: Segoe UI (system font). Code: Consolas or fallback monospace.', res_style))

    return story

def main():
    styles = getSampleStyleSheet()
    # Ensure monospaced 'Code' style exists
    if 'Code' not in styles:
        styles.add(ParagraphStyle('Code', fontName='Courier', fontSize=9, leading=11))
    # Register Segoe UI and Consolas from Windows Fonts if available, with graceful fallback
    def register_font_if_exists(name, filenames):
        for fn in filenames:
            # common system font folder on Windows
            possible = os.path.join('C:\\Windows\\Fonts', fn)
            if os.path.exists(possible):
                try:
                    pdfmetrics.registerFont(TTFont(name, possible))
                    return True
                except Exception:
                    continue
        return False

    # Attempt to register common Segoe UI variants and Consolas
    register_font_if_exists('SegoeUI', ['segoeui.ttf', 'SegoeUI.ttf', 'segoeui.ttf'])
    register_font_if_exists('SegoeUI-Bold', ['segoeuib.ttf', 'segoeuibd.ttf'])
    register_font_if_exists('Consolas', ['consola.ttf', 'Consola.ttf'])
    doc = SimpleDocTemplate(
        FILENAME,
        pagesize=A4,
        leftMargin=1.4*cm, rightMargin=1.4*cm,
        topMargin=1.4*cm, bottomMargin=1.4*cm
    )

    # Footer with page numbers
    def draw_page_number(canvas, doc):
        page_num_text = f"Page {doc.page}"
        canvas.saveState()
        canvas.setFont('SegoeUI' if 'SegoeUI' in pdfmetrics.getRegisteredFontNames() else 'Helvetica', 9)
        width, height = A4
        canvas.drawCentredString(width/2.0, 1*cm/2.0, page_num_text)
        canvas.restoreState()

    story = build_story(styles)
    doc.build(story, onFirstPage=draw_page_number, onLaterPages=draw_page_number)
    print(f"Generated {FILENAME}")

if __name__ == "__main__":
    main()
