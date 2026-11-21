# Mobile app

iOS and Android apps from one codebase.

Last reviewed: 2026-11-21

## Pick

| Layer | Choice |
|---|---|
| Framework | **Expo** (React Native) + **TypeScript** |
| Navigation | **Expo Router** (file-based) |
| Builds / updates | **EAS Build** + **EAS Update** (over-the-air fixes) |
| Styling | NativeWind (Tailwind for React Native) or StyleSheet |
| Tests | **jest-expo** + **React Native Testing Library**; **Maestro** for end-to-end flows |
| Lint / format | ESLint + Prettier |

## Why

- Expo is the toolchain the React Native team itself recommends. Managed native config, cloud builds and OTA updates are the default starting point.
- If you know React or TypeScript, you ship faster than with a new language, and you can share code and skills with a web app.
- With React Native's New Architecture, the performance gap with Flutter has narrowed a lot for typical apps.

## Setup

```bash
npx create-expo-app@latest . --template default
npx expo install expo-router
npm install -D jest-expo @testing-library/react-native prettier
```

Add `"test": "jest"`, `"typecheck": "tsc --noEmit"` and `"lint": "expo lint"` scripts, then `python3 .claude/hooks/tack detect --write`.

## Checks

lint `npm run lint` · typecheck `npm run typecheck` · test `npm run test`

## Avoid

- The bare React Native CLI for new apps, unless you have a specific native requirement Expo can't meet.
- Shipping JS-only fixes through the app stores when EAS Update can deliver them.

## Alternatives

- **Flutter**: pixel-identical custom UI everywhere, animation-heavy apps, or first-class web output, if you're happy to learn Dart.
- **Native (Swift / Kotlin)**: deep platform integration or maximum performance on one platform.

## Sources

- [Flutter vs Expo (MobiLoud)](https://www.mobiloud.com/blog/flutter-vs-expo)
- [React Native vs Flutter in 2026: when each one wins](https://dev.to/astraedus/react-native-vs-flutter-in-2026-when-each-one-actually-wins-ac4)
- [React Native in 2026: stack choices vs Flutter](https://pasqualepillitteri.it/en/news/8279/react-native-2026-stack-choices-vs-flutter)
