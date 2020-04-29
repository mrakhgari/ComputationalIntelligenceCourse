Attribute VB_Name = "Scatterplot"
' A macro for color labels in scatter plot
' _MuhmdrezA
' 9631001

Option Explicit
Const sizeOfMarker As Integer = 5

' Column 1 contains X values
' Column 2 contains Y values
' Column 3 contains label and color code

Public Sub DrawScatterplot()

Dim sheet As Worksheet
Set sheet = ActiveSheet

Dim data As Range
Set data = Selection

Dim firstRow As Integer
Dim lastRow As Integer
Dim firstColumn As Integer
Dim lastColumn As Integer

firstRow = data.Row
firstColumn = data.Column

Dim lastCell As Range
Set lastCell = data.End(xlToRight)
lastColumn = lastCell.Column
Set lastCell = data.End(xlDown)
lastRow = lastCell.Row

Dim rows As Integer
rows = lastRow - firstRow + 1
Dim columns As Integer
columns = lastColumn - firstColumn + 1

' Identify the range containing the plot data
Dim scatterData As Range
Set scatterData = Range(Cells(firstRow, firstColumn), Cells(firstRow + rows - 1, firstColumn + 1))

' Identify the ranges containing labels, symbols and colors
Dim labels As Range
Dim pointColors As Range

Set labels = Range(Cells(firstRow, firstColumn + 2), Cells(firstRow + rows - 1, firstColumn + 3))
Set pointColors = Range(Cells(firstRow, firstColumn + 2), Cells(firstRow + rows - 1, firstColumn + 3))

Charts.Add
ActiveChart.ChartType = xlXYScatter
ActiveChart.SetSourceData Source:=scatterData
ActiveChart.Location Where:=xlLocationAsObject, Name:=sheet.Name
ActiveChart.HasLegend = False
ActiveChart.PlotArea.Interior.Color = xlNone

' Add and format Gridlines
With ActiveChart.Axes(xlCategory)
    .HasMajorGridlines = True
    .HasMinorGridlines = False
End With
With ActiveChart.Axes(xlCategory).MajorGridlines.Border
    .ColorIndex = 16
    .Weight = xlHairline
    .LineStyle = xlDot
End With
    
With ActiveChart.Axes(xlValue)
    .HasMajorGridlines = True
    .HasMinorGridlines = False
End With
With ActiveChart.Axes(xlValue).MajorGridlines.Border
    .ColorIndex = 16
    .Weight = xlHairline
    .LineStyle = xlDot
End With

' Iterate over each point of the first series:
' add a label, format marker style and color.
Dim i As Integer
With ActiveChart.SeriesCollection(1)
    .ApplyDataLabels
    For i = 1 To rows
        With .Points(i)
            .DataLabel.Text = ""
            .MarkerBackgroundColorIndex = (pointColors.Cells(i, 1).Value2) * 2 + 3  ' 0 label -> red and 1 label -> blue
            .MarkerForegroundColorIndex = (pointColors.Cells(i, 1).Value2) * 2 + 3
            .markerSize = sizeOfMarker
        End With
    Next
End With

End Sub
