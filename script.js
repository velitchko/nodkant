const fs = require('fs');
const path = require('path');

const dataDir = path.join(__dirname, 'data');

// Function to check for cliques, fans, and cycles
function analyzeGraph(graph) {
    const nodes = Object.keys(graph);
    const edges = Object.values(graph).flat();

    // Check for cliques
    const isClique = nodes.every(node => {
        const neighbors = graph[node];
        return neighbors.length === nodes.length - 1 && neighbors.every(neighbor => graph[neighbor].includes(node));
    });

    // Check for fans
    const isFan = nodes.some(node => graph[node].length > nodes.length / 2);

    // Check for cycles
    const visited = new Set();
    const hasCycle = (node, parent) => {
        visited.add(node);
        for (const neighbor of graph[node]) {
            if (!visited.has(neighbor)) {
                if (hasCycle(neighbor, node)) return true;
            } else if (neighbor !== parent) {
                return true;
            }
        }
        return false;
    };
    const isCycle = nodes.some(node => !visited.has(node) && hasCycle(node, null));

    return isClique || isFan || isCycle;
}

// Read and analyze JSON files
fs.readdir(dataDir, (err, files) => {
    if (err) {
        console.error('Error reading directory:', err);
        return;
    }

    files.forEach((file, index) => {
        if(index >= 1000) return;

        if (path.extname(file) === '.json') {
            const filePath = path.join(dataDir, file);
            fs.readFile(filePath, 'utf8', (err, data) => {
                if (err) {
                    console.error('Error reading file:', err);
                    return;
                }

                try {
                    const graph = JSON.parse(data);
                    if (analyzeGraph(graph)) {
                        console.log(file);
                    }
                } catch (e) {
                    console.error('Error parsing JSON:', e);
                }
            });
        }
    });
});