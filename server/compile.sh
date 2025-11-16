(
cd ..
mkdir -p src/lib/pack
echo "export const devices = {};" >src/lib/pack/kiri-devs.js
npm install
npm run setup
npm run webpack-src prod
)
