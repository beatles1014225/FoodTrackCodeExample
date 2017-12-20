import dxfgrabber
import random
class LinesFeatures(object):
    def __init__(self,dxfPathFile, lineLpPathFile):
        self.path = dxfPathFile
        self.dxf = dxfgrabber.readfile(dxfPathFile)
        self.outputEntities = [entity for entity in self.dxf.entities]
        self.lineLpPath = lineLpPathFile

    # Read start coordinates from a DXF file which have as a type "LINE"
    def linexyzCoordinatesStartVertex(self):
        list_of_verticesStart = [entity.start for entity in self.outputEntities if entity.dxftype == 'LINE']
        return(list_of_verticesStart)

    # Read end coordinates from a DXF file which have as a type "LINE"
    def linexyzCoordinatesEndVertex(self):
        list_of_verticesEnd = [entity.end for entity in self.outputEntities if entity.dxftype == 'LINE']
        return(list_of_verticesEnd)

    # Read layers from a DXF file which have as a type "LINE"
    def layerList(self):
        layers = []
        all_lines = [entity for entity in self.dxf.entities if entity.dxftype == 'LINE']
        for line in all_lines:
            layers.append(line.layer.lower())
        return(layers)

    # Read layers from a DXF file which have as a type "LWPOLYLINE"
    def layerListPolyline(self):
        layers = []
        all_lines = [entity for entity in self.dxf.entities if entity.dxftype == 'LWPOLYLINE']
        for line in all_lines:
            layers.append(line.layer.lower())
        return(layers[1])

    # Convert "LWPOLYLINE" type to "LINE"
    def PolylineToLine(self):
        linexyCoordinatesVertex = []
        list_of_polylines = [entity.points for entity in self.outputEntities if entity.dxftype == 'LWPOLYLINE']

        for polylines in list_of_polylines:
            for vertex in polylines:
                linexyCoordinatesVertex.append((vertex + (random.uniform(29.000, 39.000),)))
        return(linexyCoordinatesVertex)

    # Assign correct heights values to each line even if lines are part of several entities
    def lineGeometryOrganization(self,linexyzCoordinatesStartVertex,linexyzCoordinatesEndVertex,lineValue):
        self.lineID = lineValue
        valueIDLayer = lineValue
        listLayers = self.layerList()
        listLayersread = []
        lpLinesFile = open(self.lineLpPath, 'w')
        referenceCoordinates = []
        for i in range(len(linexyzCoordinatesStartVertex)):
            if not "section" in listLayers[i]:
                linesVertexStart = linexyzCoordinatesStartVertex[i]
                linesVertexEnd = linexyzCoordinatesEndVertex[i]
                if i == 0:
                    heightStart = random.uniform(29.000, 30.000)
                    heightEnd = random.uniform(29.000, 30.000)
                else:
                    startHeightAssessment = self.binary_search(referenceCoordinatesSorted,linesVertexEnd[1])
                    endHeightAssessment = self.binary_search(referenceCoordinatesSorted,linesVertexStart[1])
                    if startHeightAssessment == False:
                        heightEnd = random.uniform(29.000, 30.000)
                    elif type(startHeightAssessment) == float:
                        heightEnd = startHeightAssessment

                    if endHeightAssessment == False:
                        heightStart = random.uniform(29.000, 30.000)
                    elif type(endHeightAssessment) == float:
                        heightStart = endHeightAssessment
                StringValuesStart = "line(l" + str(self.lineID) + ", " + '"' + str(linesVertexStart[0]) + '"' + ", " + '"' + \
                                    str(linesVertexStart[1]) + '"' + ", " + '"' + str(heightStart) + '"' + ", "

                StringValuesEnd = '"' + str(linesVertexEnd[0]) + '"' + ", " + '"' + str(linesVertexEnd[1]) + '"' + ", " + \
                                  '"' + str(heightEnd) + '"' + ").\n"
                StringValue = StringValuesStart + StringValuesEnd
                valueIDLayer = self.indexIDLines(listLayersread, listLayers[i], valueIDLayer)
                declarativeValues = (listLayers[i] + "(" + listLayers[i] + str(valueIDLayer) + ").\n")
                representationValues = ( "representation" + "(" + listLayers[i] + str(valueIDLayer) + "," + "l" + str(self.lineID) + ").\n")

                lpLinesFile.write(StringValue)
                lpLinesFile.write(declarativeValues)
                lpLinesFile.write(representationValues)

                self.lineID += 1
                listLayersread.append(listLayers[i])
                referenceCoordinates.append((linesVertexStart[1],heightStart))
                referenceCoordinates.append((linesVertexEnd[1], heightEnd))
                referenceCoordinatesSorted = sorted(referenceCoordinates,key=lambda x: x[0])

            else:
                break
        lpLinesFile.close()
        print("lines lp file created")

    # Assign correct heights values to each line even if lines are part of several entities
    def lineGeometryOrganizationOtherPipes(self,linexyzCoordinatesStartVertex,linexyzCoordinatesEndVertex,lineValue):
        self.lineID = lineValue
        valueIDLayer = lineValue
        listLayers = self.layerList()
        listLayersread = []
        lpLinesFile = open(self.lineLpPath, 'w')
        referenceCoordinates = []
        for i in range(len(linexyzCoordinatesStartVertex)):
            if not "section" in listLayers[i]:
                linesVertexStart = linexyzCoordinatesStartVertex[i]
                linesVertexEnd = linexyzCoordinatesEndVertex[i]
                if i == 0:
                    heightStart = random.uniform(29.700, 30.700)
                    heightEnd = random.uniform(29.700, 30.700)
                else:
                    startHeightAssessment = self.binary_search(referenceCoordinatesSorted,linesVertexEnd[1])
                    endHeightAssessment = self.binary_search(referenceCoordinatesSorted,linesVertexStart[1])
                    if startHeightAssessment == False:
                        heightEnd = random.uniform(29.700, 30.700)
                    elif type(startHeightAssessment) == float:
                        heightEnd = startHeightAssessment

                    if endHeightAssessment == False:
                        heightStart = random.uniform(29.700, 30.700)
                    elif type(endHeightAssessment) == float:
                        heightStart = endHeightAssessment
                StringValuesStart = "line(l" + str(self.lineID) + ", " + '"' + str(linesVertexStart[0]) + '"' + ", " + '"' + \
                                    str(linesVertexStart[1]) + '"' + ", " + '"' + str(heightStart) + '"' + ", "

                StringValuesEnd = '"' + str(linesVertexEnd[0]) + '"' + ", " + '"' + str(linesVertexEnd[1]) + '"' + ", " + \
                                  '"' + str(heightEnd) + '"' + ").\n"
                StringValue = StringValuesStart + StringValuesEnd
                valueIDLayer = self.indexIDLines(listLayersread, listLayers[i], valueIDLayer)
                declarativeValues = ("other_pipes" + "(" + listLayers[i] + str(valueIDLayer) + ").\n")
                typeService = ("service_other_pipe" + "(" + listLayers[i] + "," + listLayers[i] + str(valueIDLayer)+").\n")
                representationValues = ( "representation" + "(" + listLayers[i] + str(valueIDLayer) + "," + "l" + str(self.lineID) + ").\n")

                lpLinesFile.write(StringValue)
                lpLinesFile.write(declarativeValues)
                lpLinesFile.write(typeService)
                lpLinesFile.write(representationValues)

                self.lineID += 1
                listLayersread.append(listLayers[i])
                referenceCoordinates.append((linesVertexStart[1],heightStart))
                referenceCoordinates.append((linesVertexEnd[1], heightEnd))
                referenceCoordinatesSorted = sorted(referenceCoordinates,key=lambda x: x[0])

            else:
                break
        lpLinesFile.close()
        print("lines lp file with other pipe services created")

    # Assign correct heights values to each line even if lines are part of several entities
    def PolylineTolineGeometryOrganization(self,linexyzCoordinatesVertex,lineValue):
        self.lineID = lineValue
        listLayers = self.layerListPolyline()
        listLayersread = []
        lpLinesFile = open(self.lineLpPath, 'w')
        for i in range(len(linexyzCoordinatesVertex)):
            if not "section" in listLayers and i < (len((linexyzCoordinatesVertex)) - 1):
                linesVertexStart = linexyzCoordinatesVertex[i]
                linesVertexEnd = linexyzCoordinatesVertex[i + 1]
                StringValuesStart = "line(l" + str(self.lineID) + ", " + '"' + str(linesVertexStart[0]) + '"' + ", " + '"' + \
                                    str(linesVertexStart[1]) + '"' + ", " + '"' + str(linesVertexStart[2]) + '"' + ", "

                StringValuesEnd = '"' + str(linesVertexEnd[0]) + '"' + ", " + '"' + str(linesVertexEnd[1]) + '"' + ", " + \
                                  '"' + str(linesVertexEnd[2]) + '"' + ").\n"
                StringValue = StringValuesStart + StringValuesEnd
                declarativeValues = str(listLayers) + "(" + str(listLayers) + str(self.lineID) + ").\n"
                representationValues = "representation" + "(" + str(listLayers) + str(self.lineID) + "," + "l" + str(self.lineID) + ").\n"

                lpLinesFile.write(StringValue)
                lpLinesFile.write(declarativeValues)
                lpLinesFile.write(representationValues)

                self.lineID += 1
                listLayersread.append(listLayers)
            else:
                break
        lpLinesFile.close()
        print("Polylines lp file created")

    # To identify lines already assigned
    def indexIDLines(self,listLayers,layer, valueIDLayer):
        if layer in listLayers and len(listLayers) == 1:
            valueIDLayer += 1
        elif layer in listLayers and listLayers[(len(listLayers) - 1)] == layer:
            valueIDLayer += 1
        elif layer in listLayers and listLayers[(len(listLayers) - 1)] != layer:
            valueIDLayer = len(listLayers) - valueIDLayer + 1
        else:
            valueIDLayer = 1
        return (valueIDLayer)

    def finalLineID(self):
        return(self.lineID)

    # To seek lines already assigned in the array lines
    def binary_search(self,array, target):
        lower = 0
        upper = len(array)
        while lower < upper:
            x = lower + (upper - lower) // 2
            val = array[x][0]
            if target == val:
                return array[x][1]
            elif target > val:
                if lower == x:
                    break
                lower = x
            elif target < val:
                upper = x
        return False



