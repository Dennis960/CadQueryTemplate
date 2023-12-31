import cadquery as cq
import math

table_plate_thickness = 20
leg_thickness = 50
leg_height = 200
blend_thickness = 20
blend_length = 100  # arbitrary value
blend_height = 50
corner_bracket_thickness = 15
corner_bracket_length = 50
screw_diameter = 4

table_leg = (cq.Workplane("XY")
             .rect(leg_thickness, -leg_thickness, centered=(False, False))
             .extrude(-leg_height)
             )
table_blend = (cq.Workplane("XY")
               .moveTo(leg_thickness, 0)
               .rect(blend_length, -blend_thickness, centered=(False, False))
               .extrude(-blend_height)
               .moveTo(0, -leg_thickness)
               .rect(blend_thickness, -blend_length, centered=(False, False))
               .extrude(-blend_height)
               )

table_plate = (cq.Workplane("XY")
               .rect(blend_length + leg_thickness, -blend_length - leg_thickness, centered=(False, False))
               .extrude(table_plate_thickness)
               )

corner_bracket = (cq.Workplane("XY")
                  .moveTo(leg_thickness, -leg_thickness)
                  .line(0, leg_thickness - blend_thickness)
                  .line(corner_bracket_length, 0)
                  .line(0, -corner_bracket_thickness)
                  .line(-corner_bracket_length + corner_bracket_thickness, 0)
                  .line(0, -leg_thickness + blend_thickness + corner_bracket_thickness)
                  .threePointArc((leg_thickness + math.sin(math.radians(45)) * corner_bracket_thickness, -leg_thickness - math.sin(math.radians(45)) * corner_bracket_thickness), (leg_thickness, -leg_thickness - corner_bracket_thickness))
                  .line(-leg_thickness + blend_thickness + corner_bracket_thickness, 0)
                  .line(0, -corner_bracket_length + corner_bracket_thickness)
                  .line(-corner_bracket_thickness, 0)
                  .line(0, corner_bracket_length)
                  .line(leg_thickness - blend_thickness, 0)
                  .close()
                  .extrude(-blend_height)
                  .moveTo(blend_thickness + 0.5 * corner_bracket_thickness, -leg_thickness - 0.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutThruAll()
                  .moveTo(leg_thickness + 0.5 * corner_bracket_thickness, -blend_thickness - 0.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutThruAll()
                  .tag("a")
                  .faces("<X")
                  .workplane(origin=(0, 0, 0))
                  .moveTo(leg_thickness + corner_bracket_length - 0.5 * corner_bracket_thickness, -0.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutThruAll()
                  .moveTo(leg_thickness + corner_bracket_length - 0.5 * corner_bracket_thickness, -blend_height + 0.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutThruAll()
                  .faces(">Y")
                  .workplane(origin=(0, 0, 0))
                  .moveTo(-leg_thickness - corner_bracket_length + 0.5 * corner_bracket_thickness, -0.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutThruAll()
                  .moveTo(-leg_thickness - corner_bracket_length + 0.5 * corner_bracket_thickness, -blend_height + 0.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutThruAll()
                  .workplaneFromTagged("a")
                  .transformed(rotate=(90, 45, 0))
                  .moveTo(0, -0.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutBlind(1000)
                  .moveTo(0, -blend_height + 0.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutBlind(1000)
                  .workplaneFromTagged("a")
                  .moveTo(leg_thickness + corner_bracket_thickness, -blend_thickness - corner_bracket_thickness)
                  .rect(corner_bracket_thickness, -corner_bracket_thickness, centered=(False, False))
                  .extrude(-corner_bracket_thickness)
                  .moveTo(leg_thickness + 1.5 * corner_bracket_thickness, -blend_thickness - 1.5 * corner_bracket_thickness)
                  .circle(screw_diameter / 2)
                  .cutThruAll()
                  .moveTo(blend_thickness + corner_bracket_thickness, -leg_thickness - corner_bracket_thickness)
                    .rect(corner_bracket_thickness, -corner_bracket_thickness, centered=(False, False))
                    .extrude(-corner_bracket_thickness)
                    .moveTo(blend_thickness + 1.5 * corner_bracket_thickness, -leg_thickness - 1.5 * corner_bracket_thickness)
                    .circle(screw_diameter / 2)
                    .cutThruAll()
                  )

corner_bracket_printable = corner_bracket.rotate((0, 0, 0), (0, 1, 0), 180)

if __name__ == "__main__":
    import ocp_vscode
    ocp_vscode.show_object(table_plate)
    ocp_vscode.show_object(table_leg)
    ocp_vscode.show_object(table_blend)
    ocp_vscode.show_object(corner_bracket)
    ocp_vscode.show_object(corner_bracket_printable)

    cq.Assembly(corner_bracket_printable, name="corner_bracket").save(
        "corner_bracket.stl")
    cq.Assembly(table_leg, name="table_leg").save("table_leg.stl")
    cq.Assembly(table_blend, name="table_blend").save(
        "table_blend.stl")
    cq.Assembly(table_plate, name="table_plate").save(
        "table_plate.stl")
