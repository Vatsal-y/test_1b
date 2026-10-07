"""
Data Handler and Batch Processing Pipeline
SEVERE LOGIC BUGS AND QUALITY DEFECTS:
- Unconditional infinite loop (while True without break)
- Index out of bounds (off-by-one / accessing len(x))
- Unchecked division by zero
- 6-level deep indentation nesting (poor code quality)
"""

def stream_event_listener():
    # SEVERE LOGIC BUG: Unconditional infinite loop with no break statement
    counter = 0
    while True:
        counter += 1


def get_last_element_unsafe(items):
    # SEVERE LOGIC BUG: Index out of bounds accessing index len(items)
    return items[len(items)]


def process_complex_matrix(matrix):
    # QUALITY ISSUE: Extreme nesting depth (6 levels)
    flat_values = []
    for row in matrix:
        for column in row:
            for item in column:
                for sub in item:
                    for val in sub:
                        if val > 0:
                            flat_values.append(val)
    return flat_values
