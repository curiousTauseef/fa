from fa.commands import utils

try:
    import idautils
except ImportError:
    pass


def get_parser():
    p = utils.ArgumentParserNoExit()
    p.add_argument('--null-terminated', action='store_true')
    return p


def max_xrefs(addresses):
    xrefs = []
    for address in addresses:
        xrefs.append((address, len([ref.frm for ref in idautils.XrefsTo(address)])))

    if len(xrefs) > 0:
        address, _ = max(xrefs, key=lambda x: x[1])
        return [address]

    return []


def run(segments, args, addresses, **kwargs):
    return max_xrefs(addresses)