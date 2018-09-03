treeData = open('../../LabsData/trees.dat')
trees = []

for tree in treeData:
    try:
        tree = int(tree)
    except ValueError:
        print 'Invalid value type - {}'.format(tree)
    else:
        trees.append(tree)
treeData.close()

print 'Number of trees: {}'.format(len(trees))
print 'Average tree height: {:.1f} ft'.format(float(sum(trees))/len(trees))
print 'Tallest tree height: {:.1f} ft'.format(max(trees))
print 'Shortest tree height: {:.1f} ft'.format(min(trees))
