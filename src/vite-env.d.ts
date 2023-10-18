/// <reference types="./vite-env-override.d.ts" />
/// <reference types="vite/client" />
declare module '*.svg' {
    const content: React.FC<React.SVGProps<SVGElement>>
    export default content
}