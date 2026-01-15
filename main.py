from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    # Verificamos si cabe por lo menos un panel dentro del techo
    condition1 = (panel_height > roof_width and panel_width > roof_width)
    condition2 = (panel_height > roof_height and panel_width > roof_height)
    if condition1 or condition2:
        return 0

    # Ahora en resumen tenemos que probar la combinación de paneles 
    # instalados de manera normal o rotados, es decir, a,b o b,a.
    # Junto con la permutacion del agregado horizontal o vertical
    # de los paneles. Llegando así al maximo posible de paneles 
    # instalados

    best = 0

    # Ahora calcularemos el caso del llenado vertical.
    # Donde el llenado se aplica primero normal y 
    # luego rotado 

    rows_normal = roof_height//panel_height
    rows_rotate = roof_height//panel_width
    colums_normal = roof_width//panel_width
    for k in range (0,colums_normal):
        stripe = roof_width-k*panel_width
        total = k*rows_normal + stripe//panel_height*rows_rotate
        best = max(best,total)
    
    # Ahora calcularemos el caso del llenado vertical.
    # Donde el llenado se aplica primero rotados y 
    # luego normales

    rows_normal = roof_height//panel_width
    rows_rotate = roof_height//panel_height
    colums_normal = roof_width//panel_height
    for k in range (0,colums_normal):
        stripe = roof_width-k*panel_height
        total = k*rows_normal + stripe//panel_width*rows_rotate
        best = max(best,total)

    # Ahora calcularemos el caso del llenado horizontal.
    # Donde el llenado se aplica primero normal y 
    # luego rotado 

    rows_normal = roof_width//panel_height
    rows_rotate = roof_width//panel_width
    colums_normal = roof_height//panel_width
    for k in range (0,colums_normal):
        stripe = roof_height-k*panel_width
        total = k*rows_normal + stripe//panel_height*rows_rotate
        best = max(best,total)
    
    # Ahora calcularemos el caso del llenado horizontal.
    # Donde el llenado se aplica primero rotados y 
    # luego normales

    rows_normal = roof_width//panel_width
    rows_rotate = roof_width//panel_height
    colums_normal = roof_height//panel_height
    for k in range (0,colums_normal):
        stripe = roof_height-k*panel_height
        total = k*rows_normal + stripe//panel_width*rows_rotate
        best = max(best,total)

    return best


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()