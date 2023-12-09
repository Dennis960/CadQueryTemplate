import cadquery as cq

obj = cq.Workplane("XY").box(1, 2, 3)

if __name__ == "__main__":
    import ocp_vscode
    ocp_vscode.show_object(obj)