import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Link):
        path, separator, fragment = elem.url.partition('#')
        if path.endswith('.md'):
            elem.url = path[:-3] + '.html'
            if separator:
                elem.url += separator + fragment
            return elem

    if isinstance(elem, pf.Header) and elem.identifier:
        elem.content.append(pf.Space())
        elem.content.append(
            pf.Link(
                pf.Str('#'),
                url=f'#{elem.identifier}',
                classes=['heading-anchor'],
            )
        )
        return elem

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
