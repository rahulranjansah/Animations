import vtk

def main():

    reader = vtk.vtkSTLReader()
    reader.SetFileName("Motion around Centre of Mass for heavenly bodies.stl")
    
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(1,1,1) # RGB values

    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == "__main__":
    main()