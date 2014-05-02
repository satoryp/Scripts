import os
import sys
#usage: python foo.py [directory to be traversed] [directory to write output] [number of subdirectory layers to traverse]
#output: filename_and_sizes.csv written to [directory to write output]

outputFilename = "filenames_and_sizes.csv"
startingDirectory = sys.argv[1]
outputDirectory = sys.argv[2]
maxLayersDeep = int(sys.argv[3])

def search_and_print_filesize(rootDirectory, layersDeep):
	global maxLayersDeep
	if layersDeep > maxLayersDeep:
		return 0
	layersDeep = layersDeep + 1
	directorySize = 0
	rootDirectory = os.path.abspath(rootDirectory)
	for file in os.listdir(rootDirectory):
		filePath = os.path.join(rootDirectory, file)
		if os.path.isfile(filePath):
			if(file is not outputFilename):
				outFile.write("{},{},{}\n".format(file, os.path.getsize(filePath), filePath))
				directorySize = directorySize + os.path.getsize(filePath)
		else:
			directorySize = directorySize + search_and_print_filesize(filePath, layersDeep)
	outFile.write("{},{},{}\n".format(os.path.basename(rootDirectory), directorySize, rootDirectory))
	return directorySize

outputDirectory = os.path.abspath(outputDirectory)
startingDirectory = os.path.abspath(startingDirectory)
outfileName = os.path.join(outputDirectory, outputFilename)
outFile = open(outfileName, 'w')
search_and_print_filesize(startingDirectory, 0)
outFile.close()