import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function SalaryCalculator() {
  const [salary, setSalary] = useState(0);
  const [result, setResult] = useState(null);

  const calculateSalary = () => {
    let bruto = parseFloat(salary);
    let CCSS = bruto * 0.1067;
    let SEM = bruto * 0.055;
    let IVM = bruto * 0.0417;
    let AporteBanco = bruto * 0.01;
    
    let impuestoRenta = 0;
    if (bruto > 922000) impuestoRenta += Math.min(bruto - 922000, 430000) * 0.10;
    if (bruto > 1352000) impuestoRenta += Math.min(bruto - 1352000, 1021000) * 0.15;
    if (bruto > 2373000) impuestoRenta += Math.min(bruto - 2373000, 2372000) * 0.20;
    if (bruto > 4745000) impuestoRenta += (bruto - 4745000) * 0.25;
    
    let totalDeducciones = CCSS + SEM + IVM + AporteBanco + impuestoRenta;
    let salarioNeto = bruto - totalDeducciones;

    let CCSSPatrono = bruto * 0.1467;
    let OtrasInst = bruto * 0.0725;
    let LeyProteccion = bruto * 0.0475;
    let totalAportes = CCSSPatrono + OtrasInst + LeyProteccion;
    let costoTotal = bruto + totalAportes;

    setResult({ bruto, CCSS, SEM, IVM, AporteBanco, impuestoRenta, totalDeducciones, salarioNeto, CCSSPatrono, OtrasInst, LeyProteccion, totalAportes, costoTotal });
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <Card className="w-full max-w-lg p-6 shadow-lg rounded-2xl bg-white">
        <h1 className="text-2xl font-bold mb-4">Calculadora de Salario (Costa Rica)</h1>
        <input
          type="number"
          className="w-full p-2 border rounded mb-4"
          placeholder="Ingrese salario bruto"
          value={salary}
          onChange={(e) => setSalary(e.target.value)}
        />
        <Button onClick={calculateSalary} className="w-full bg-blue-600 text-white p-2 rounded">Calcular</Button>
        {result && (
          <CardContent className="mt-4">
            <h2 className="text-xl font-semibold">Resultados:</h2>
            <p>Salario Bruto: ₡{result.bruto.toLocaleString()}</p>
            <p>CCSS: ₡{result.CCSS.toLocaleString()}</p>
            <p>SEM: ₡{result.SEM.toLocaleString()}</p>
            <p>IVM: ₡{result.IVM.toLocaleString()}</p>
            <p>Aporte Banco Popular: ₡{result.AporteBanco.toLocaleString()}</p>
            <p>Impuesto de Renta: ₡{result.impuestoRenta.toLocaleString()}</p>
            <p className="font-bold">Total Deducciones: ₡{result.totalDeducciones.toLocaleString()}</p>
            <p className="text-green-600 font-bold">Salario Neto: ₡{result.salarioNeto.toLocaleString()}</p>
            <hr className="my-2" />
            <p>CCSS Patrono: ₡{result.CCSSPatrono.toLocaleString()}</p>
            <p>Otras Instituciones: ₡{result.OtrasInst.toLocaleString()}</p>
            <p>Ley Protección Trabajador: ₡{result.LeyProteccion.toLocaleString()}</p>
            <p className="font-bold">Total Aportes Patrono: ₡{result.totalAportes.toLocaleString()}</p>
            <p className="text-red-600 font-bold">Costo Total: ₡{result.costoTotal.toLocaleString()}</p>
          </CardContent>
        )}
      </Card>
    </div>
  );
}
