# Diagrams (Mingrammer)

1. Instalar choco. Abrir `Powershell` como admin

```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) 
```
2. Instalar `grahpviz`

```bash
choco install graphviz
```

**Nota:** Si estas en MacOs o Linuz debes usar estos pasos [Instalacion](https://diagrams.mingrammer.com/docs/getting-started/installation)

3.  Instalar `Diagrams` con 
```bash
pip install diagrams
```

Es recomendable tener `python3.6` o superior

4. Listo ya se pueden generar diagramas. Automaticamente se exportan.

```python
# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
```

# Go Diagrams

1. Iniciar proyecto con:
```bash
mkdir go_diagrams
cd go_diagrams
go mod init go_diagrams_v1
```

2. Instalar complemento
```bash
go get github.com/blushft/go-diagrams@latest
```

3. Crear el archivo `main.go`
```go
package main
import (
	"log"

	"github.com/blushft/go-diagrams/diagram"
	"github.com/blushft/go-diagrams/nodes/gcp"
)
func main() {
	d, err := diagram.New(diagram.Filename("app"), diagram.Label("App"), diagram.Direction("LR"))
	if err != nil {
		log.Fatal(err)
	}

	dns := gcp.Network.Dns(diagram.NodeLabel("DNS"))
	lb := gcp.Network.LoadBalancing(diagram.NodeLabel("NLB"))
	cache := gcp.Database.Memorystore(diagram.NodeLabel("Cache"))
	db := gcp.Database.Sql(diagram.NodeLabel("Database"))

	dc := diagram.NewGroup("GCP")
	dc.NewGroup("services").
		Label("Service Layer").
		Add(
			gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 1")),
			gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 2")),
			gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 3")),
		).
		ConnectAllFrom(lb.ID(), diagram.Forward()).
		ConnectAllTo(cache.ID(), diagram.Forward())

	dc.NewGroup("data").Label("Data Layer").Add(cache, db).Connect(cache, db)

	d.Connect(dns, lb, diagram.Forward()).Group(dc)

	if err := d.Render(); err != nil {
		log.Fatal(err)
	}

	// Add the following lines to render the diagram
	if err := d.Render(); err != nil {
		log.Fatal(err)
	}
}

```
4. Luego de que se genere el grafico simpelmente con  `graphViz` se puede crear el plot final
```bash
dot app.dot -Tpng -o app.png
```
O si prefieres otro formato

```bash
dot .\k8s.dot -Tjpeg -o k8s.jpeg
```

5. 